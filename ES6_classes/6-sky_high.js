/* eslint-disable no-unused-vars */
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  // eslint-disable-next-line constructor-super
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors.`;
  }
}
