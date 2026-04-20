## Linting

More importantly than any "blessed" set of linters, lint consistently across a
codebase.

We recommend using the following linters at a minimum, because we feel that they
help to catch the most common issues and also establish a high bar for code
quality without being unnecessarily prescriptive:

- [errcheck](https://github.com/kisielk/errcheck) to ensure that errors are handled
- [goimports](https://pkg.go.dev/golang.org/x/tools/cmd/goimports) to format code and manage imports
- [revive](https://github.com/mgechev/revive) to point out common style mistakes
- [govet](https://pkg.go.dev/cmd/vet) to analyze code for common mistakes
- [staticcheck](https://staticcheck.dev) to do various static analysis checks

  > **Note**: [revive](https://github.com/mgechev/revive) is the modern, faster successor to the now-deprecated [golint](https://github.com/golang/lint).

### Lint Runners

We recommend [golangci-lint](https://github.com/golangci/golangci-lint) as the go-to lint runner for Go code, largely due
to its performance in larger codebases and ability to configure and use many
canonical linters at once. This repo has an example [.golangci.yml](https://github.com/uber-go/guide/blob/master/.golangci.yml) config file
with recommended linters and settings.

golangci-lint has [various linters](https://golangci-lint.run/usage/linters/) available for use. The above linters are
recommended as a base set, and we encourage teams to add any additional linters
that make sense for their projects.
