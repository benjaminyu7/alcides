import Head from 'next/head'
import ChatBox from '@/components/chatbox/chatbox'
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { blue, orange } from '@mui/material/colors';

const theme = createTheme({
  palette: {
    primary: blue,
    secondary: orange,
    contrastThreshold: 4.5,
  },
});

export default function Home() {

  return (
    <>
      <Head>
        <title>Alcides</title>
        <meta name="description" content="Collaborate with chat" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div>
          <ThemeProvider theme={theme}>
            <ChatBox />
          </ThemeProvider>
        </div>
      </main>
    </>
  )
}
