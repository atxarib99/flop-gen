import React, {Component, useEffect} from "react";
import * as deck from '@letele/playing-cards';
import {List, Button, Snackbar} from '@mui/material'; 
import Slide, { SlideProps } from '@mui/material/Slide';

type GeneratedProps = {
	generated: String[];
	hand?: ["1d", "1c", "1s", "1h"];
};

function SlideTransition(props: SlideProps) {
  return <Slide {...props} direction="up" />;
}

function GeneratedOutput(props: GeneratedProps) {

  const [open, setOpen] = React.useState(false);
	const [snackbarMessage, setMessage] = React.useState("");

  const handleClose = (event: React.SyntheticEvent | Event, reason?: string) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };

	function stringToCards(str: String): string[] {

		const Cards: string[] = []; 
		str.match(/.{1,2}/g)?.forEach(val => {
			const remappedStr = val.substring(1,2).toUpperCase() + val.substring(0,1).toLowerCase().replace('t', '10');
			Cards.push(remappedStr);
		});

		return Cards;
	}
	
	function useCopyClick() {
		copyToClipboard(props.generated.toString());
	};

	const copyToClipboard = (str) => {
		const el = document.createElement("textarea");
		el.value = str;
		el.setAttribute("readonly", "");
		el.style.position = "absolute";
		el.style.left = "-9999px";
		document.body.appendChild(el);
		try {
			const selected =
				document.getSelection().rangeCount > 0
					? document.getSelection().getRangeAt(0)
					: false;
			el.select();
			document.execCommand("copy");
			document.body.removeChild(el);
			if (selected) {
				document.getSelection().removeAllRanges();
				document.getSelection().addRange(selected);
			}
			setMessage("Copied!");
			setOpen(true);

		} catch(e: unknown) {
			setMessage("Couldn't copy!");
			setOpen(true);
		}
	};
	

	return (
		<div className="fullWidth">
			<Button variant="contained" onClick={useCopyClick}>
				Copy
			</Button>
			<List
				sx={{
					width: '100%',
					bgcolor: '#EEEEEE',
					position: 'relative',
					overflow: 'auto',
					height: '100vh',
					'& ul': { padding: 0 },
				}}
				subheader={<li />}
			>	
				{
					props.generated.map((val, index) => {
						const Cards = stringToCards(val);
						return (
							<div>
								{Cards.map((val2, index) => {
									const Card = deck[val2];
									return (
										<Card style={{ height: '10%', width: '10%' }} />	
									)
								})}
							</div>
						)})
				}
			</List>

			<Snackbar
      anchorOrigin={{ vertical:'bottom', horizontal:'center'}}
			open={open}
			autoHideDuration={2000}
			onClose={handleClose}
			message={snackbarMessage}
			TransitionComponent={Slide}
			/>	
		</div>
	);

}

export default GeneratedOutput;
