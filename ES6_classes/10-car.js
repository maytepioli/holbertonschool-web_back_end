// eslint-disable-next-line no-unused-vars
const cloneSymbol = Symbol('clone');

export default class Car {
  constructor(brand, color, motor) {
    this._brand = brand;
    this._color = color;
    this._motor = motor;
  }

  [cloneSymbol]() {
    return new (Object.getPrototypeOf(this).constructor)(this._brand, this._motor, this._color);
  }

  cloneCar() {
    return this[cloneSymbol]();
  }
}
