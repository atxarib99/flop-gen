import React from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem } from "@mui/material";
import FilterSelect from "./FilterSelect";

function App() {
  const textureOptions = ["rainbow", "two-tone", "monotone"];

  return (
    <div className="App">
      <header className="App-header"></header>
      <body className="App-body">
        <div>
          <FilterSelect filterName="texture" filterOptions={textureOptions} />

          <FilterSelect filterName="texture2" filterOptions={textureOptions} />
        </div>
      </body>
    </div>
  );
}

export default App;
