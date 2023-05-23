# Nighty Wheels

This repository contains code to build a bunch of lab-cosmo Python projects each
day, and make the pre-built wheels directly installable with pip.

- https://github.com/lab-cosmo/librascal

```
pip install --extra-index-url http://luthaf.fr/nightly-wheels/ rascal
```


## Adding a new project

1. copy one of the workflow in `.github/workflows` to `<new-project.yml>` and
   edit it to build the wheels in the `build-wheels` job
2. open a PR with these changes, make sure CI passes and merge it
3. add the new project folder to the `index.html` file on the gh-pages branch
