export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  String() {
    return `Airport _name: ${this._name}, _code: ${this._code}`;
  }
}