# Builder Method

Training Builder Method with Python.

## Annotations

![alt UML Builder Method](https://github.com/hedibertosilva/design-patterns-python/blob/main/builder-method/contents/uml.png?raw=true)

- The Director class is a cookbook that it has a pre-set of full products.
- The Director class is a bridge to connect to the Builder class.
- The Builder class separates the application to the Car (concrete product).
- The Builder class has all options available to construct the Car (concrete product).
- The method "reset" (Builder class) returns a new Car (concrete product).
- The method "get_result" (Builder class) connect the application to the product output.

This method allows to builder complex products without complex structure class and isolate the final product code to the application.

## Requirements

- Python >= 3.7

## Usage

```sh
python3 -u builder-method
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)