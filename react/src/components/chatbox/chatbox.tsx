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

  const [message, setMessage] = useState("Initial Message: ");
  const [inputValue, setInputValue] = useState("Initial Message: ");

  function handleClick() {
    setMessage(inputValue)
    setInputValue('')
  }

  function handleInputChange(event: any) {
    setInputValue(event.target.value)
  }

  function handleKeyDown(event: any) {
    if (event.keyCode == 13 && !event.shiftKey) {
      event.preventDefault();
      handleClick()
    }
  }

  return (
    <div className ={styles.chatbox}>
      <Card>
        <TextBox avatar='a' text={message}/>
        <Box id={styles.chatBoxtextFieldBox}>
          <TextField
              multiline
              maxRows={4}
              fullWidth
              onChange={handleInputChange} 
              value={inputValue}
              onKeyDown={handleKeyDown}
          />
          <IconButton onClick={handleClick}>
            <SendIcon />
          </IconButton>
        </Box>
      </Card>
    </div>
  );
}