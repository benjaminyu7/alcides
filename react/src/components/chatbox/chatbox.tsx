import * as React from 'react';
import { useState } from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import TextField from '@mui/material/TextField';
import styles from '@/styles/components/chatbox.module.css'  
import TextBox from '@/components/chatbox/textbox'
import SendIcon from '@mui/icons-material/Send';
import IconButton from '@mui/material/IconButton';

export default function ChatBox() {

  const [messages, setMessages]:[JSX.Element[], Function] = useState([]);
  const [inputValue, setInputValue]:[String, Function] = useState("");

  function sendMessage() {
    var newMessages = messages
    newMessages.push(<TextBox avatar='a' text={inputValue}/>)
    setMessages(newMessages)
    setInputValue('')
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