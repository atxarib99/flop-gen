import React from "react";
import PlayingCardsList from "./PlayingCard/Hand/PlayingCard/PlayingCardsList";

type GeneratedProps = {
	generated: object;
};

function GeneratedOutput(props: GeneratedProps) {


	return (
		<div>
			<Hand hide={false} layout={"spread"} cards={this.state.hand} cardSize={this._getCardSize()}/> 
		</div>
	);

}

export default GeneratedOutput;
