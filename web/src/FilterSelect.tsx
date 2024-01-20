import React from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem } from "@mui/material";

type FilterProps = {
  filterName: string;
  filterOptions: Array<string>;
};

function FilterSelect(props: FilterProps) {
  const [filterName, setFilterName] = React.useState(props.filterName);
  const [filterVal, setFilter] = React.useState("");
  const [filterOptions, setAvailableOptions] = React.useState(
    props.filterOptions
  );

  const handleChange = (event: SelectChangeEvent) => {
    setFilter(event.target.value as string);
  };

  return (
    <div className="filter-div">
      <Box display="flex">
        <FormControl fullWidth>
          <InputLabel id="demo-simple-select-label">{filterName}</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={filterVal}
            label={filterName}
            className="filter-form"
            onChange={handleChange}
          >
            {filterOptions.map((filterOption) => {
              return <MenuItem value={filterOption}>{filterOption}</MenuItem>;
            })}
          </Select>
        </FormControl>
      </Box>
    </div>
  );
}

export default FilterSelect;
