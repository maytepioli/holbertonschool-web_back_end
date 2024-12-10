// eslint-disable-next-line import/extensions
import Car from './10-car.js';

class TestCar extends Car {}

const tc1 = new TestCar('Nissan', 'Turbo', 'Pink');
const tc2 = tc1.cloneCar();

// eslint-disable-next-line jest/require-hook
console.log(tc1);
// eslint-disable-next-line jest/require-hook
console.log(tc1 instanceof TestCar);

// eslint-disable-next-line jest/require-hook
console.log(tc2);
// eslint-disable-next-line jest/require-hook
console.log(tc2 instanceof TestCar);

// eslint-disable-next-line jest/require-hook, eqeqeq
console.log(tc1 == tc2);
