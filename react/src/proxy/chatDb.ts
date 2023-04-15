export function CreateMessage (sender: string, recipient: string, message:string, createMessage: Function) {
    fetch(`/flask/addMessage/${sender}/${recipient}`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({'message': message})
    })
    .then(res => {
        if(res.ok) {
            res.json()
        } else {
            alert('Error!')
            throw new Error()
        }
    })
}

export function GetMessage (sender: string, recipient: string, createMessage:Function) {
    fetch(`/flask/getMessages/${sender}/${recipient}`, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
    })
    .then(res => res.json())
    .then(
        (result) => {
            if(result.messages != null) {
                createMessage(result.messages)
            }
        }
    );
}