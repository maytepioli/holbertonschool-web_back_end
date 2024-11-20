import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    if (!(currency instanceof Currency)) {
      throw Error('The currency parameter must be an instance of the Currency class');
    }
    this._amont = amount;
    this._currency = currency;
  }

  get amount() {
    return this._amont;
  }

  set amount(valor) {
    this._amont = valor;
  }

  get currency() {
    return this._currency;
  }

  set currency(valor) {
    this._currency = valor;
  }

  displayFullPrice() {
    return `${this._amont} ${this._currency._name} (${this._currency._code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
