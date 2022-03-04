# Factory Method

Training Factory Method with Python.

## Annotations

![alt UML Factory Method](https://github.com/hedibertosilva/design-patterns-python/blob/main/factory-method/content/uml.jpg?raw=true)

- Concrete Products populates the setter method (Concrete Factory);
- Setter method (Concrete Factory) calls set_color method (Concrete Product);
- Setter method (Concrete Factory) returns a concrete product;
- Decorate method calls buy method (Abstract Factory);
- Buy method (Abstract Factory) calls setter method;
- Buy method (Abstract Factory) calls make method (Concrete Product)
- Buy method (Abstract Factory) returns a concrete product;

## Requirements

- Python >= 3.7

## Usage

```sh
python3 -u factory-method
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)