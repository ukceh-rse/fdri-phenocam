# Phenocam image processing

[![tests badge](https://github.com/ukceh-rse/fdri-phenocam/actions/workflows/pipeline.yml/badge.svg)](https://github.com/ukceh-rse/fdri-phenocam/actions)
[![docs badge](https://github.com/ukceh-rse/fdri-phenocam/actions/workflows/deploy-docs.yml/badge.svg)](https://ukceh-rse.github.io/fdri-phenocam/)

[Read the docs!](https://ukceh-rse.github.io/fdri-phenocam)

This repository is an experimental version of image processing pipelines for the Phenocam images on COSMOS-UK sensors. 
It was created using the [UKCEH python project template](https://github.com/NERC-CEH/python-template) and repurposes some of the pipeline code in [plankton_ml](https://github.com/NERC-CEH/python-template). It is intended for rapid prototyping and use case refinement.

### Note on dependency versions

We're using the [thingsvision](https://github.com/ViCCo-Group/thingsvision) package to simplify extracting features from different computer vision models.
It currently requires python <3.11 and numpy <2. If the approach stays useful, it makes sense to remove `thingsvision` in favour of model-specific code.

## Getting Started

### Using the Githook

From the root directory of the repo, run:

```
git config --local core.hooksPath .githooks/
```

This will set this repo up to use the git hooks in the `.githooks/` directory. The hook runs `ruff format --check` and `ruff check` to prevent commits that are not formatted correctly or have errors. The hook intentionally does not alter the files, but informs the user which command to run.

### Installing the package

This package is configured to use optional dependencies based on what you are doing with the code.

As a user, you would install the code with only the dependencies needed to run it:

```
pip install .
```

To work on the docs:

```
pip install -e .[docs]
```

To work on tests:

```
pip install -e .[tests]
```

To run the linter and githook:

```
pip install -e .[lint]
```

The docs, tests, and linter packages can be installed together with:

```
pip install -e .[dev]
```

### Building Docs Locally

The documentation is driven by [Sphinx](https://www.sphinx-doc.org/) an industry standard for documentation with a healthy userbase and lots of add-ons. It uses `sphinx-apidoc` to generate API documentation for the codebase from Python docstrings.

To run `sphinx-apidoc` run:

```
# Install your package with optional dependencies for docs
pip install -e .[docs]

cd docs
make apidoc
```

This will populate `./docs/sources/...` with `*.rst` files for each Python module, which may be included into the documentation.

Documentation can then be built locally by running `make html`, or found on the [GitHub Deployment](https://ukceh-rse.github.io/fdri-phenocam).

### Run the Tests

To run the tests run:

```
#Install package with optional dependencies for testing
pip install -e .[test]

pytest
```

### Automatic Versioning

This codebase is set up using [autosemver](https://autosemver.readthedocs.io/en/latest/usage.html#) a tool that uses git commit history to calculate the package version. Each time you make a commit, it increments the patch version by 1. You can increment by:

* Normal commit. Use for bugfixes and small updates
    * Increments patch version: `x.x.5 -> x.x.6`
* Commit starts with `* NEW:`. Use for new features
    * Increments minor version `x.1.x -> x.2.x`
* Commit starts with `* INCOMPATIBLE:`. Use for API breaking changes
    * Increments major version `2.x.x -> 3.x.x`


 
