public class Human {
    int age;
    String name;

    public Human(int age, String name) {
        this.age = age;
        this.name = name;
    }

    public void print(){
        System.out.println("Human with name " + name + " and age " + age + "years.");
    }
}
