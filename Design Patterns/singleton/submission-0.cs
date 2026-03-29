public class Singleton {

    private string value = "a value string";
    private static Singleton instance = null;

    private Singleton() {
      
    }

    public static Singleton getInstance() {
        if(instance == null) {
            instance = new Singleton();
        }
        return instance;
        

    }

    public string getValue() {
        return value;
    }

    public void setValue(string value){
        this.value = value;
    }
}
