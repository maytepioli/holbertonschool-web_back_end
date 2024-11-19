export default class HolbertonCourse {
  // Función de validación reutilizable
  static validateType(value, expectedType, attributeName) {
    if (typeof value !== expectedType) {
      throw new TypeError(`${attributeName} must be a ${expectedType}`);
    }
  }

  constructor(name, length, students) {
    // Usar la función de validación para verificar los tipos
    HolbertonCourse.validateType(name, 'string', 'name');
    this._name = name;

    HolbertonCourse.validateType(length, 'number', 'length');
    this._length = length;

    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw new TypeError('students must be an Array');
    }
  }

  // Getter para 'name'
  get name() {
    return this._name;
  }

  // Setter para 'name'
  set name(value) {
    HolbertonCourse.validateType(value, 'string', 'name');
    this._name = value;
  }

  // Getter para 'length'
  get length() {
    return this._length;
  }

  // Setter para 'length'
  set length(value) {
    HolbertonCourse.validateType(value, 'number', 'length');
    this._length = value;
  }

  // Getter para 'students'
  get students() {
    return this._students;
  }

  // Setter para 'students'
  set students(value) {
    if (Array.isArray(value)) {
      this._students = value;
    } else {
      throw new TypeError('students must be an Array');
    }
  }
}
