import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import styles from '@/styles/components/chatbox.module.css'  
import Avatar from '@mui/material/Avatar';

export default function TextBox(props: any) {
  return (
    <Card className={styles.textbox}>
      <CardContent>
        <Avatar>{props.avatar}</Avatar>
      </CardContent>
      <Typography>
        {props.text}
      </Typography>
    </Card>
  );
}