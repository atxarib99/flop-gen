import React from "react";
import "./App.css";
import Box from "@mui/system/Box";
import Select, { SelectChangeEvent } from "@mui/material/Select";
import FormControl from "@mui/material/FormControl";
import { InputLabel, MenuItem, IconButton } from "@mui/material";
import ClearIcon from '@mui/icons-material/Clear';

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

	onClearClicked = () => {
		this.setState({filterVal: ''});
	}

  render() {
		return(
			<div id={this.props.id} className="filter-div">
				<Box sx={{ flexDirection: 'row', width:'100%', display:'inline-block' }}>
					<FormControl className="formControl" fullWidth>
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
						<IconButton className="clearButton" color="primary" onClick={this.onClearClicked}>
							<ClearIcon/>
						</IconButton>
					</FormControl>
				</Box>
			</div>
		);
  };
}

export default FilterSelect;
