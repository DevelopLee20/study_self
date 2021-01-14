class Person {
  String _name;

  String get name => _name;
  set name(String name) => _name = name;
}

main() {
  Person person = Person();
  person.name = "Kim";
  print(person.name);
}
