<script>
    import { onMount } from "svelte";

    let participants = [];
    let countries = ["Suomi", "Ruotsi", "Norja"];
    let selected_country = "",
        men = true,
        women = true;
    let filteredParticipants = [];

    onMount(async () => {
        try {
            const response = await fetch("./src/participants.json");
            console.log(response);
            participants = await response.json();
            console.log(participants);
            countries = [
                ...new Set(
                    participants.map((participant) => participant.kansallisuus),
                ),
            ];
            myFilter();
        } catch (error) {
            console.error(error);
        }
    });

    let myFilter = () => {
        filteredParticipants = participants;
        if (selected_country !== "") {
            filteredParticipants = filteredParticipants.filter(
                (participant) => participant.kansallisuus === selected_country,
            );
        }
        if (!men) {
            filteredParticipants = filteredParticipants.filter(
                (participant) => participant.sarja !== "M",
            );
        }
        if (!women) {
            filteredParticipants = filteredParticipants.filter(
                (participant) => participant.sarja !== "N",
            );
        }
    };
</script>

<div
    style="display: inline-flex; background-color: gainsboro; border:solid darkgray 2pt;"
>
    <a href="/#/" style="font-size: 2em; margin-top: 17pt;">🔙</a>
    <h1 style="font:bold 2em tahoma;">Participants</h1>
</div>
<div
    style="background-color: darkgrey;
    display: flex; flex-direction: column; justify-content: center; padding-left: 1em;"
>
    <p style="margin: 1em; font: 1em tahoma;">
        Here are the participants of the event. You can apply filters to filter
        the list.
    </p>
    <div>
        <select bind:value={selected_country} on:change={myFilter}>
            <option value="">Filter by country</option>
            {#each countries as country}
                <option value={country}>{country}</option>
            {/each}
        </select>
    </div>
    <div>
        <label>
            <input type="checkbox" bind:checked={men} on:change={myFilter} />
            Men
        </label>

        <label>
            <input type="checkbox" bind:checked={women} on:change={myFilter} />
            Women
        </label>
    </div>
    <div
        style="background-color: darkgrey; padding: 1em;
        display: flex; flex-direction: column; justify-content: center;"
    >
        <table>
            <tr>
                <th>Number</th><th>Name</th><th>Nationality</th><th>Class</th>
            </tr>
            {#each filteredParticipants as participant (participant.numero)}
                <tr>
                    <td>{participant.numero}</td>
                    <td>{participant.nimi}</td>
                    <td>{participant.kansallisuus}</td>
                    <td>{participant.sarja}</td>
                </tr>
            {/each}
        </table>
    </div>
</div>

<style>
    tr,
    td,
    th {
        border: 1px solid black;
        padding: 5px;
    }
</style>
