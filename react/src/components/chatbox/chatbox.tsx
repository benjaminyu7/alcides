import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import TextField from '@mui/material/TextField';
import styles from '@/styles/components/chatbox.module.css'  
import TextBox from '@/components/chatbox/textbox'

export default function ChatBox() {
  return (
    <Card sx={{ minWidth: 275 }}>
      <TextBox avatar='a' text='text'/>
      <Box id={styles.chatBoxtextFieldBox}>
        <TextField
            multiline
            maxRows={4}
            fullWidth 
        />
      </Box>
    </Card>
  );
}