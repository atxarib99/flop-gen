import React from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem, Button } from "@mui/material";
import FilterSelect from "./FilterSelect";

function App() {
	//todo create an api that returns a json packages of available filters from the engine
  const textureOptions = ["rainbow", "two-tone", "monotone"];
	const suitOptions = ["Club", "Spade", "Heart", "Diamond"];
	const highestCardOptions = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"];
	const connectivityOptions = ["disconnected", "semi_connected_low", "semi_connected_high", "connected"];
	const pairingOptions = ["unpaired", "paired", "tripled"];

	const generateClick = () => {
		alert('Generate!');
	}

  return (
    <div className="App">
      <header className="App-header"></header>
      <body className="App-body">
        <div>
          <FilterSelect filterName="texture" filterOptions={textureOptions} />
          <FilterSelect filterName="suit" filterOptions={suitOptions} />
          <FilterSelect filterName="highestCard" filterOptions={highestCardOptions} />
          <FilterSelect filterName="connectivity" filterOptions={connectivityOptions} />
          <FilterSelect filterName="pairing" filterOptions={pairingOptions} />
					<Button variant="contained" onClick={generateClick}>
						Generate!
					</Button>
					
        </div>
      </body>
    </div>
  );
}

export default App;
