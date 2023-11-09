## Introduction to LinkML

Slides for the presentation can be found [here](https://docs.google.com/presentation/d/1IGZZlSCj0nP4zujDiNg6NYyM9ysxwAfOgThH0glpIGg/edit?usp=sharing)

A simple hands-on example was prepared based on the [linkml tutorial](https://linkml.io/linkml/intro/tutorial.html) and [Person Schema example](https://github.com/linkml/linkml/tree/main/examples/PersonSchema).

The initial version of the schema is called `personinfo.yaml` and the "final" version of the example can be found in `personinfo_final.yaml`.

### Installation

In order to run the example you should install `linkml`.

```
python3 -m venv linkml_env
source linkml_env/bin/activate
pip install linkml
```

### Running linkml linter

To run a basic check of the schema you can run `linkml-lint`:

```
linkml-lint --validate personinfo.yaml
```

### Running linkml generators

In order to convert the schema to different formats you can run linkml generators, e.g:

- JSON Schema
  ```
  gen-json-schema personinfo.yaml > outputs/personinfo.schema.json
  ```

- Python-pydantic
  ```
  gen-pydantic personinfo.yaml outputs/personinfo.py
  ```

- ER diagram
  ```
  gen-erdiagram personinfo.yaml > outputs/personinfo.md
  ```


