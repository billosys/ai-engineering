"use strict";

const form = document.querySelector("#visit-form");
const fields = document.querySelector("#request-fields");
const submitButton = document.querySelector("#submit-request");
const errorSummary = document.querySelector("#error-summary");
const errorList = document.querySelector("#error-list");
const errorItemTemplate = document.querySelector("#error-item-template");
const pendingStatus = document.querySelector("#pending-status");
const serviceError = document.querySelector("#service-error");
const serviceErrorTitle = document.querySelector("#service-error-title");
const unavailableToggle = document.querySelector("#simulate-unavailable");
const draftUnavailableToggle = document.querySelector("#simulate-draft-unavailable");
const confirmation = document.querySelector("#confirmation");
const confirmationTitle = document.querySelector("#confirmation-title");
const editButton = document.querySelector("#edit-request");
const saveDraftButton = document.querySelector("#save-draft");
const restoreDraftButton = document.querySelector("#restore-draft");
const clearDraftButton = document.querySelector("#clear-draft");
const draftStatus = document.querySelector("#draft-status");
const draftMessageCopy = document.querySelector("#draft-message-copy");

const nameInput = document.querySelector("#visitor-name");
const emailInput = document.querySelector("#visitor-email");
const windowSelect = document.querySelector("#visit-window");
const countSelect = document.querySelector("#visitor-count");

const formFields = [
  {
    control: nameInput,
    hintId: "name-hint",
    errorId: "name-error",
    labelId: "label-for-visitor-name",
    invalid: () => nameInput.value.trim() === "",
  },
  {
    control: emailInput,
    hintId: "email-hint",
    errorId: "email-error",
    labelId: "label-for-visitor-email",
    invalid: () => emailInput.value.trim() === "" || !emailInput.validity.valid,
  },
  {
    control: windowSelect,
    hintId: "window-hint",
    errorId: "window-error",
    labelId: "label-for-visit-window",
    invalid: () => !["am-101", "pm-202"].includes(windowSelect.value) || !windowSelect.validity.valid,
  },
  {
    control: countSelect,
    hintId: "count-hint",
    errorId: "count-error",
    labelId: "label-for-visitor-count",
    invalid: () => !["1", "2", "3", "4", "5", "6"].includes(countSelect.value) || !countSelect.validity.valid,
  },
];

let requestInProgress = false;
const draftStorageKey = "design-library-visit-draft";
const draftMaximumLength = 16384;
const draftLifetimeMs = 24 * 60 * 60 * 1000;

function updateDraftControlAvailability() {
  const unavailable = requestInProgress || !confirmation.hidden;
  saveDraftButton.disabled = unavailable;
  restoreDraftButton.disabled = unavailable;
  clearDraftButton.disabled = false;
}

function showDraftStatus(messageKey, isError = false) {
  const message = draftMessageCopy.content.querySelector(`[data-message="${messageKey}"]`);
  draftStatus.replaceChildren(...Array.from(message.childNodes, (node) => node.cloneNode(true)));
  draftStatus.classList.toggle("is-error", isError);
  draftStatus.hidden = false;
}

function getDraftStorage() {
  if (draftUnavailableToggle.checked) {
    throw new Error("Draft storage is unavailable in this simulation.");
  }

  return window.sessionStorage;
}

function saveDraft() {
  const draft = {
    schema: 1,
    savedAt: Date.now(),
    fields: {
      name: nameInput.value,
      email: emailInput.value,
      visit: windowSelect.value,
      visitors: countSelect.value,
    },
  };
  const serialized = JSON.stringify(draft);

  if (serialized.length > draftMaximumLength) {
    showDraftStatus("save-too-large", true);
    return;
  }

  try {
    const storage = getDraftStorage();
    storage.setItem(draftStorageKey, serialized);
    showDraftStatus("saved");
  } catch {
    showDraftStatus("save-failed", true);
  }
}

function hasExactKeys(value, expectedKeys) {
  if (value === null || typeof value !== "object" || Array.isArray(value)) {
    return false;
  }

  const keys = Object.keys(value);
  return keys.length === expectedKeys.length && expectedKeys.every((key) =>
    Object.prototype.hasOwnProperty.call(value, key)
  );
}

function isValidDraft(value, now) {
  if (!hasExactKeys(value, ["schema", "savedAt", "fields"])) {
    return false;
  }

  if (
    value.schema !== 1 ||
    !Number.isFinite(value.savedAt) ||
    !Number.isInteger(value.savedAt) ||
    value.savedAt < 0 ||
    value.savedAt > now ||
    now - value.savedAt > draftLifetimeMs ||
    !hasExactKeys(value.fields, ["name", "email", "visit", "visitors"])
  ) {
    return false;
  }

  const { name, email, visit, visitors } = value.fields;
  return typeof name === "string" &&
    typeof email === "string" &&
    ["", "am-101", "pm-202"].includes(visit) &&
    ["", "1", "2", "3", "4", "5", "6"].includes(visitors);
}

function restoreDraft() {
  let rawDraft;

  try {
    const storage = getDraftStorage();
    rawDraft = storage.getItem(draftStorageKey);
  } catch {
    showDraftStatus("read-failed", true);
    return;
  }

  if (rawDraft === null) {
    showDraftStatus("missing");
    return;
  }

  if (typeof rawDraft !== "string" || rawDraft.length > draftMaximumLength) {
    showDraftStatus("invalid-too-large", true);
    return;
  }

  let parsedDraft;
  try {
    parsedDraft = JSON.parse(rawDraft);
  } catch {
    showDraftStatus("invalid-json", true);
    return;
  }

  if (!isValidDraft(parsedDraft, Date.now())) {
    showDraftStatus("expired-or-invalid", true);
    return;
  }

  const { name, email, visit, visitors } = parsedDraft.fields;
  nameInput.value = name;
  emailInput.value = email;
  windowSelect.value = visit;
  countSelect.value = visitors;
  updateFieldErrors([]);
  renderErrorSummary([]);
  serviceError.hidden = true;
  nameInput.focus();
  showDraftStatus("restored");
}

function clearDraft() {
  try {
    const storage = getDraftStorage();
    storage.removeItem(draftStorageKey);
    showDraftStatus("cleared");
  } catch {
    showDraftStatus("clear-failed", true);
  }
}

function clearDraftAfterCompletion() {
  try {
    const storage = getDraftStorage();
    storage.removeItem(draftStorageKey);
    showDraftStatus("completion-cleared");
  } catch {
    showDraftStatus("completion-clear-failed", true);
  }
}

function updateFieldErrors(invalidFields) {
  for (const field of formFields) {
    const isInvalid = invalidFields.includes(field);
    const error = document.querySelector(`#${field.errorId}`);
    field.control.setAttribute("aria-describedby", isInvalid ? `${field.hintId} ${field.errorId}` : field.hintId);

    if (isInvalid) {
      field.control.setAttribute("aria-invalid", "true");
    } else {
      field.control.removeAttribute("aria-invalid");
    }

    error.hidden = !isInvalid;
  }
}

function renderErrorSummary(invalidFields) {
  errorList.replaceChildren();

  for (const field of invalidFields) {
    const item = errorItemTemplate.content.firstElementChild.cloneNode(true);
    const link = item.querySelector("a");
    const label = document.querySelector(`#${field.labelId}`);
    const message = document.querySelector(`#${field.errorId}`);

    link.href = `#${field.control.id}`;
    item.querySelector("[data-field-label]").textContent = label.textContent.trim();
    const messageCopy = message.querySelector(".error-copy");
    item.querySelector("[data-field-message]").replaceChildren(
      ...Array.from(messageCopy.childNodes, (node) => node.cloneNode(true))
    );
    link.addEventListener("click", (event) => {
      event.preventDefault();
      field.control.focus();
    });
    errorList.append(item);
  }

  errorSummary.hidden = invalidFields.length === 0;
}

function showConfirmation(snapshot) {
  document.querySelector("#confirmation-name").textContent = snapshot.name;
  document.querySelector("#confirmation-email").textContent = snapshot.email;
  document.querySelector("#confirmation-window").textContent = snapshot.visitWindow;
  document.querySelector("#confirmation-count").textContent = snapshot.visitorCount;
  document.querySelector("#confirmation-reference").textContent = snapshot.referenceCode;
  form.hidden = true;
  confirmation.hidden = false;
  updateDraftControlAvailability();
  confirmationTitle.focus();
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  if (requestInProgress) {
    return;
  }

  serviceError.hidden = true;

  const invalidFields = formFields.filter((field) => field.invalid());
  updateFieldErrors(invalidFields);
  renderErrorSummary(invalidFields);

  if (invalidFields.length > 0) {
    errorSummary.focus();
    return;
  }

  const snapshot = {
    name: nameInput.value.trim(),
    email: emailInput.value,
    visitWindow: windowSelect.selectedOptions[0].textContent,
    visitorCount: countSelect.selectedOptions[0].textContent,
    referenceCode: windowSelect.value === "am-101" ? "AM-101" : "PM-202",
  };
  const simulateUnavailable = unavailableToggle.checked;

  requestInProgress = true;
  fields.disabled = true;
  submitButton.disabled = true;
  updateDraftControlAvailability();
  pendingStatus.hidden = false;
  pendingStatus.focus();

  window.setTimeout(() => {
    requestInProgress = false;
    pendingStatus.hidden = true;

    if (simulateUnavailable) {
      fields.disabled = false;
      submitButton.disabled = false;
      updateDraftControlAvailability();
      serviceError.hidden = false;
      serviceErrorTitle.focus();
      return;
    }

    clearDraftAfterCompletion();
    showConfirmation(snapshot);
  }, 800);
});

editButton.addEventListener("click", () => {
  confirmation.hidden = true;
  form.hidden = false;
  fields.disabled = false;
  submitButton.disabled = false;
  serviceError.hidden = true;
  updateDraftControlAvailability();
  nameInput.focus();
});

saveDraftButton.addEventListener("click", saveDraft);
restoreDraftButton.addEventListener("click", restoreDraft);
clearDraftButton.addEventListener("click", clearDraft);

fields.disabled = false;
submitButton.disabled = false;
updateDraftControlAvailability();
