import React, {Component, useEffect} from "react";
import * as deck from '@letele/playing-cards';
import List from '@mui/material/List';

type GeneratedProps = {
	generated: String[];
	hand?: ["1d", "1c", "1s", "1h"];
};

function GeneratedOutput(props: GeneratedProps) {

	function stringToCards(str: String): string[] {

		const Cards: string[] = []; 
		str.match(/.{1,2}/g)?.forEach(val => {
			console.log(1);
			console.log(val);
			const remappedStr = val.substring(1,2).toUpperCase() + val.substring(0,1).toLowerCase().replace('t', '10');
			Cards.push(remappedStr);
		});

		return Cards;
	}

	return (
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
					console.log(Cards);
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
	);

}

export default GeneratedOutput;
