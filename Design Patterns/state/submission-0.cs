public interface IState {
    void HandleRequest(Document doc);
}

public class Document {
    private IState state;
    private bool isApproved;
    public IState? PrevState {get; set;} = null;

    public Document() {
        this.state = new Draft();
    }

    public IState GetState() {
        return this.state;
    }

    public void SetState(IState state) {
        this.state = state;
    }

    public void Publish() {
        this.state.HandleRequest(this);
    }

    public void SetApproval(bool isApproved) {
        this.isApproved = isApproved;
    }

    public bool IsApproved() {
        return this.isApproved;
    }
}

public class Draft : IState {
    public void HandleRequest(Document doc) {
        if(doc.PrevState == null || doc.PrevState.GetType() == typeof(Review)) {
            doc.PrevState = doc.GetState();
            doc.SetState(new Review());
        }
    }
}

public class Review : IState {
    public void HandleRequest(Document doc) {
        if(doc.PrevState.GetType() == typeof(Draft) && doc.IsApproved()) {
            doc.PrevState = doc.GetState();
            doc.SetState(new Published());
        }
        else if(doc.PrevState.GetType() == typeof(Draft) && !doc.IsApproved()) {
            doc.PrevState = doc.GetState();
            doc.SetState(new Draft());
        }
    }
}

public class Published : IState {
    public void HandleRequest(Document doc) {
        // Write your code here
    }
}
