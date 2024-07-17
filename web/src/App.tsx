import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem, Button } from "@mui/material";
import FilterSelect from "./FilterSelect";
import GeneratedOutput from "./GeneratedOutput";


type Filter = {
	name: string;
	selection: string;
	inverted: boolean;
};

function App() {
	//todo create an api that returns a json packages of available filters from the engine
  const textureOptions = ["rainbow", "two-tone", "monotone"];
	const suitOptions = ["Club", "Spade", "Heart", "Diamond"];
	const highestCardOptions = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"];
	const connectivityOptions = ["disconnected", "semi_connected_low", "semi_connected_high", "connected"];
	const pairingOptions = ["unpaired", "paired", "tripled"];


	const [filters, setFilters] = React.useState<Array<{}>>([]);
	const [selectedFilters, setSelectedFilters] = React.useState<Array<{}>>([]);
	const [generatedFlops, setFlops] = React.useState<Array<String>>([]);
	const filterRefs = useRef<(FilterSelect | null)[]>([]);

	useEffect(() => {
		console.log('loaded');
		fetch('http://127.0.0.1:3001/flop-gen/v1/filters')
		.then(response => response.json())
		.then(data => {
			console.log(data);
			setFilters(data);}
		)
		.catch(error => console.log(error));
	}, []);
	
	type CharIterator = (str: string) => string;

	const camelToUnderScore: CharIterator = (str) => {
		let output = "";
		str.split('').forEach(char => {
			if (char == char.toUpperCase()) {
				output += '_';
				output += char.toLowerCase();
			} else {
				output += char;
			}
		});

		return output.substring(1);
	};

	const useGenerateClick = async () => {
		let filters: Filter[] = [];
		Array.from(Array(filterRefs.current.length).keys()).map((val, index) => {
			var currRef = filterRefs.current[val];
			if(currRef) {
				if(currRef.state.filterVal) {
					var curFilter: Filter = {
						name: camelToUnderScore(currRef.props.filterName),
						selection: currRef.state.filterVal,
						inverted: false
					};
					filters.push(curFilter);
				}
			}
		});
		console.log('Generating...');
		await fetch('http://127.0.0.1:3001/flop-gen/v1/generate',{
			method: 'POST',
			body: JSON.stringify({'filters': filters, 'engine': {'flops': 10, 'weights': false}}),
			headers: {
      "Content-Type": "application/json",
			},
		})
		.then(response => response.json())
		.then(data => { console.log(data); setFlops(data);})
		.catch(error => console.log(error));
	}


  return (
    <div className="App">
      <header className="App-header"></header>
      <body className="App-body">
        <div className="row">
					<div className="column">
						{
							filters.map((val,index) => {
								return (
									<FilterSelect ref={(ref) => filterRefs.current[index] = ref} id={val['name']} filterName={val['name']} filterOptions={val['options']} />
								)
							})
						}
						<Button className="generateButton" id="generateButton" variant="contained" onClick={useGenerateClick}>
							Generate!
						</Button>
					</div>
					<div className="column">
						{ generatedFlops && <GeneratedOutput generated={generatedFlops}/> }
					</div>
					
        </div>
      </body>
    </div>
  );
}

export default App;
