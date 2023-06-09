import './App.css';
import { useEffect, useState } from 'react';
import { BrowserRouter, Routes, Route, NavLink } from 'react-router-dom';

function App() {
	const [ressponse, setRessponse] = useState([])
	const [fetchd, setfetchd] = useState(true)

	const HandleSingleForm = (e) => {
		e.preventDefault();
		let id = e.target.id.value;
		let method = e.target.method.value;
		fetch(`http://127.0.0.1:8000/api/v3/app/events/${id}`, {
			method: method,
		}).then(res => res.json())
			.then(data => {
				console.log(data);
				setRessponse(data)
				if (data.length) {
					var inputs = document.getElementById("submit-form").querySelectorAll("input[type='text'], input[type='number'], input[type='datetime-local'], textarea")
					inputs.forEach((input) => {
						if (input.type === "datetime-local") {
							input.value = data[0][input.name].slice(0, -1);
						} else {
							input.value = data[0][input.name]
						}
					})
				}
			})
	}

	const HandleMultipleForm = (e) => {
		e.preventDefault();
		var data = new FormData(e.target)
		console.log(data);
		// make a put request to uppdate data  at `http://127.0.0.1:8000/api/v3/app/events/${id}``http://127.0.0.1:8000/api/v3/app/events/${id}`
		fetch(`http://127.0.0.1:8000/api/v3/app/events/${data.get('id')}`, {
			method: 'PUT',
			body: data,
		}).then(res => res.json()).then(data => {
			console.log(data);
			setfetchd(!fetchd)
		}
		).catch(error => console.error(error));
	}
	const HandleMultipleFormCreate = (e) => {
		e.preventDefault();
		var data = new FormData(e.target)
		console.log(data);
		// make a put request to uppdate data  at `http://127.0.0.1:8000/api/v3/app/events/${id}``http://127.0.0.1:8000/api/v3/app/events/${id}`
		fetch(`http://127.0.0.1:8000/api/v3/app/events`, {
			method: 'POST',
			body: data,
		}).then(res => res.json()).then(data => {
			console.log(data);
			setfetchd(!fetchd)
		}
		).catch(error => console.error(error));
	}

	useEffect(() => {
		fetch("http://127.0.0.1:8000/api/v3/app/events?limit=100").then(res => res.json()).then(data => setRessponse(data))
	}, [fetchd])
	const DeleteItem = (id) => {
		fetch(`http://127.0.0.1:8000/api/v3/app/events/${id}`, {
			method: "DELETE",
		})
		setRessponse(ressponse.filter((item) => item.id !== id))
	}
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/single" element={
					<div className="App">
						<div className="data">
						{ressponse.map((event) => {
								return <div class="event">
									<div class="avatar">
										<p class="id">{event.id}</p>
										<img src={`http://127.0.0.1:8000${event.file}`} alt="" />
									</div>
									<div class="info">
										{/* <div className="keyvalue">
											<p className='key'>Rigor Rank</p>
											<p class="tagline">{event.rigor_rank}</p>
										</div> */}
										<div className="keyvalue">
											<p className='key'>name</p>
											<p class="tagline">{event.name}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>tagline</p>
											<p class="tagline">{event.tagline}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>schedule</p>
											<p class="tagline">{event.schedule}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>Attendees</p>
											<p class="tagline">{event.attendees.map((data)=>data.trim().charAt(0).toUpperCase() + data.trim().slice(1)+",")}</p>
										</div>
										<div class="operations">
											<button onClick={() => DeleteItem(event.id)} >Delete</button>
										</div>
									</div>
								</div>
							})}
						</div>
						<div className="form">
							<h3>Retrive, Update and Delete</h3>
							<div className="mylinks">

								<NavLink to="/">List And Create</NavLink>
								<NavLink to="/single">Retrive, Update and Delete</NavLink>
							</div>
							<Single HandleSingleForm={HandleSingleForm} />
							<Multiple HandleMultipleForm={HandleMultipleForm} />
						</div>
					</div>
				} />
				<Route path="/" element={
					<div className="App">
						<div className="data">
							{ressponse.map((event) => {
								return <div class="event">
									<div class="avatar">
										<p class="id">{event.id}</p>
										<img src={`http://127.0.0.1:8000${event.file}`} alt="" />
									</div>
									<div class="info">
										{/* <div className="keyvalue">
											<p className='key'>Rigor Rank</p>
											<p class="tagline">{event.rigor_rank}</p>
										</div> */}
										<div className="keyvalue">
											<p className='key'>name</p>
											<p class="tagline">{event.name}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>tagline</p>
											<p class="tagline">{event.tagline}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>schedule</p>
											<p class="tagline">{event.schedule}</p>
										</div>
										<div className="keyvalue">
											<p className='key'>Attendees</p>
											<p class="tagline">{event.attendees.map((data)=>data.trim().charAt(0).toUpperCase() + data.trim().slice(1)+",")}</p>
										</div>
										<div class="operations">
											<button onClick={() => DeleteItem(event.id)} >Delete</button>
										</div>
									</div>
								</div>
							})}
						</div>
						<div className="form">
							<h3>List And Create</h3>
							<div className="mylinks">
								<NavLink to="/">List And Create</NavLink>
								<NavLink to="/single">Retrive, Update and Delete</NavLink>
							</div>
							<Multiple HandleMultipleForm={HandleMultipleFormCreate} />
						</div>
					</div>
				} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;


const Single = ({ HandleSingleForm }) => {
	return <div className="retrive">
		<form id="retrive-form" onSubmit={HandleSingleForm}>
			<label htmlFor="id">ID:</label>
			<input type="number" id="id" name="id" required />
			<label htmlFor="method">Select Method:</label>
			<select name="method">
				<option value="GET">GET</option>
				<option value="DELETE">DELETE</option>
			</select> <br />
			<button className='sub_btn' type="submit">Get Event</button>
		</form>
	</div>
}
const Multiple = ({ HandleMultipleForm }) => {
	return <form id="submit-form" onSubmit={HandleMultipleForm} encType="multipart/form-data">
		<label htmlFor="id">id:</label>
		<input type="text" id="id" name="id" required />

		<label htmlFor="event_type">Event Type:</label>
		<input type="text" id="event_type" name="event_type" required />

		<label htmlFor="name">Name:</label>
		<input type="text" id="name" name="name" required />

		<label htmlFor="tagline">Tagline:</label>
		<input type="text" id="tagline" name="tagline" required />

		<label htmlFor="schedule">Schedule:</label>
		<input type="datetime-local" id="schedule" name="schedule" />

		<label htmlFor="description">Description:</label>
		<textarea id="description" name="description" required></textarea>

		<label htmlFor="file">Image File:</label>
		<input type="file" id="file" name="file" required />

		<label htmlFor="user">User</label>
		<input type="text" id="user" name="user" required />

		<label htmlFor="Category">Category</label>
		<input type="text" id="Category" name="Category" required />

		<label htmlFor="Subcategory">Subcategory</label>
		<input type="text" id="Subcategory" name="Subcategory" required />

		<label htmlFor="rigor_rank">Rigor Rank:</label>
		<input type="number" id="rigor_rank" name="rigor_rank" required />

		<label htmlFor="attendees">Attendees:</label>
		<input type="text" id="attendees" name="attendees" required /><br></br>

		<button className='sub_btn' type="submit">Update data</button>
	</form>
}