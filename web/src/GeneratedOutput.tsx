import React from "react";
import * as deck from '@letele/playing-cards';

type GeneratedProps = {
	generated: {};
	hand?: ["1d", "1c", "1s", "1h"];
};

function GeneratedOutput(props: GeneratedProps) {

	const Card = deck['Sq']

	return (
		<div>
			<Card style={{ height: '100%', width: '100%' }} />	
		</div>
	);

}

export default GeneratedOutput;
