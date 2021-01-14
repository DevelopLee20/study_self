class Person {
  Person() {
    print("This is Person Constructor!");
  }
}

class Student extends Person {
  Student() {
    print("This is Student Constructor!");
  }
}

main() {
  // not in use error
  // var person = Student();
  Student();
}
