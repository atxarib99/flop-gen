import React from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem } from "@mui/material";

type FilterProps = {
  filterName: string;
  filterOptions: Array<string>;
	id: string;
};

type FilterSelectState = {
	filterVal: string;
}

class FilterSelect extends React.Component<FilterProps, FilterSelectState> {

	state: FilterSelectState = {
		filterVal: "",
	};

  handleChange = (event: SelectChangeEvent) => {
		this.setState({filterVal: event.target.value});
  };

  render() {
		return(
			<div id={this.props.id} className="filter-div">
				<Box display="flex">
					<FormControl fullWidth>
						<InputLabel id="demo-simple-select-label">{this.props.filterName}</InputLabel>
						<Select
							labelId="demo-simple-select-label"
							id="demo-simple-select"
							value={this.state.filterVal}
							label={this.props.filterName}
							className="filter-form"
							onChange={this.handleChange}
						>
							{this.props.filterOptions.map((filterOption) => {
								return <MenuItem value={filterOption}>{filterOption}</MenuItem>;
							})}
						</Select>
					</FormControl>
				</Box>
			</div>
		);
  };
}

export default FilterSelect;
