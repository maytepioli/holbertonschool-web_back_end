// eslint-disable-next-line import/extensions
import SkyHighBuilding from './6-sky_high.js';

const building = new SkyHighBuilding(140, 60);
// eslint-disable-next-line jest/require-hook
console.log(building.sqft);
// eslint-disable-next-line jest/require-hook
console.log(building.floors);
// eslint-disable-next-line jest/require-hook
console.log(building.evacuationWarningMessage());
