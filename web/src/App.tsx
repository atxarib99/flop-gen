import React, { useState, useEffect, useRef } from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem, Button, Checkbox, FormControlLabel, TextField } from "@mui/material";
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
	const [checked, setChecked] = useState(false);

	const [numFlops, setNumFlops] = useState(10);
  	const [numFlopsError, setNumFlopsError] = useState('');


	useEffect(() => {
		console.log('loaded');
		fetch('http://0.0.0.0:3001/flop-gen/v1/filters')
		.then(response => response.json())
		.then(data => {
			console.log(data);
			setFilters(data);}
		)
		.catch(error => console.log(error));
	}, []);

	const handleWeightsChange = (event) => {
		setChecked(event.target.checked);
	};

	const handleNumFlopsChange = (event) => {
	    const input = event.target.value;
	    // Check if input is a number
	    if (!isNaN(input)) {
	      const num = parseInt(input, 10);
	      // Check if number is within limits (example limits: 0 to 100)
	      if (num >= 1 && num <= 100) {
		setNumFlops(num);
		setNumFlopsError('');
	      } else {
		setNumFlopsError('Number must be between 0 and 100');
	      }
	    } else {
	      setNumFlopsError('Please enter a valid number');
	    }
	  };
	
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
		await fetch('http://0.0.0.0:3001/flop-gen/v1/generate',{
			method: 'POST',
			body: JSON.stringify({'filters': filters, 'engine': {'flops': numFlops, 'weights': checked}}),
			headers: {
      "Content-Type": "application/json",
			},
		})
		.then(response => response.json())
		.then(data => { console.log(data); setFlops(data);})
		.catch(error => console.log(error));
	}

  //make second div classname = row on big widths
  return (
    <div className="App">
      <header className="App-header"></header>
      <body className="App-body">
        <div className="row">
					<div className="column">
						<h3> Filters </h3>
						{
							filters.map((val,index) => {
								return (
									<FilterSelect ref={(ref) => filterRefs.current[index] = ref} id={val['name']} filterName={val['name']} filterOptions={val['options']} />
								)
							})
						}
						<div className="row">
							<div className="column">
							<h3> Engine Parameters </h3>
							</div>
						</div>

						<div className="centeredRow">
							<FormControlLabel control={<Checkbox disabled onChange={handleWeightsChange} />} label="Weights" />
						      <TextField
							type="number"
							label="Flops"
							value={numFlops}
							onChange={handleNumFlopsChange}
							error={!!numFlopsError}
							helperText={numFlopsError}
							inputProps={{
							  min: 1,
							  max: 100,
							  step: 1,
							}}
							variant="outlined"
							margin="normal"
						      />



						</div>
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
