import * as React from 'react';
import { useState, useEffect } from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import TextField from '@mui/material/TextField';
import styles from '@/styles/components/chatbox.module.css'  
import TextBox from '@/components/chatbox/textbox'
import SendIcon from '@mui/icons-material/Send';
import IconButton from '@mui/material/IconButton';
import { GetMessage, CreateMessage } from '@/proxy/chatDb';
import { MESSAGE_CONTENT, MESSAGE_SENDER } from '@/constants/databaseConstants';

export default function ChatBox() {

  const [messages, setMessages]:[JSX.Element[], Function] = useState([]);
  const [inputValue, setInputValue]:[string, Function] = useState("");
  const sender = "anySender";
  const recipient = "anyRecipient";

  function sent(result: any) {console.log(result)}

  function addMessage(thisMessages: {message_content:string, sender: string}[]) {
    var newMessages = messages.slice();
    for(var index in thisMessages) {
      newMessages.push(<TextBox avatar='a' text={thisMessages[index][MESSAGE_CONTENT]}/>)
    }
    setMessages(newMessages)
  }

  function sendMessage() {
    if(inputValue!=='') {
      CreateMessage(sender, recipient,inputValue,sent)
      addMessage([{message_content: inputValue, sender: sender}])
      setInputValue('')
    }
  }

  function handleInputChange(event: any) {
    setInputValue(event.target.value)
  }

  function handleKeyDown(event: any) {
    if (event.keyCode == 13 && !event.shiftKey) {
      event.preventDefault();
      sendMessage()
    }
  }

  useEffect(() => {
    GetMessage(recipient, addMessage)
  }, [])

  return (
    <div className ={styles.chatbox}>
      <Card>
        <div>{messages}</div>
        
        <Box id={styles.chatBoxtextFieldBox}>
          <TextField
              multiline
              maxRows={4}
              fullWidth
              onChange={handleInputChange} 
              value={inputValue}
              onKeyDown={handleKeyDown}
          />
          <IconButton onClick={sendMessage}>
            <SendIcon />
          </IconButton>
        </Box>
      </Card>
    </div>
  );
}