<script>
    let newOsallistuja = {
        etunimi: "",
        sukunimi: "",
        id: "",
        kansallisuus: "",
        sarja: "",
    };
    let existing = [];
    function clear() {
        newOsallistuja = {
            etunimi: "",
            sukunimi: "",
            id: "",
            kansallisuus: "",
            sarja: "",
        };
    }
    function save() {
        fetch(`http://localhost:5000/osallistujat/${newOsallistuja.id}`)
            .then((response) => response.json())
            .then((data) => {
                if (data.exists) {
                    // ID exists in the database
                    alert("Kilpailija on jo olemassa");
                } else {
                    // ID does not exist in the database
                    fetch(
                        `http://localhost:5000/osallistujat/${newOsallistuja.id}`,
                        {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json",
                            },
                            body: JSON.stringify(newOsallistuja),
                        },
                    )
                        .then((response) => response.json())
                        .then((data) => {
                            if (data.error) {
                                alert(data.error);
                            } else {
                                alert("Kilpailija lisätty onnistuneesti");
                            }
                        })
                        .catch((error) => console.error("Error:", error));
                }
            })
            .catch((error) => console.error("Error:", error));
    }
</script>

<h1>Lisää uusi kilpailija</h1>

<form>
    Kilpailijan nimi:
    <input
        bind:value={newOsallistuja.etunimi}
        class="syöttö"
        type="text"
        placeholder="Etunimi"
    />
    <input
        bind:value={newOsallistuja.sukunimi}
        class="syöttö"
        type="text"
        placeholder="Sukunimi"
    />
    <input
        bind:value={newOsallistuja.id}
        class="syöttö"
        type="text"
        placeholder="Numero"
    />
    <input
        bind:value={newOsallistuja.kansallisuus}
        class="syöttö"
        type="text"
        placeholder="Kansallisuus"
    />
    <label for="sarja">Sarja:</label>
    <div>
        <label for="N">Naiset</label>
        <input
            id="N"
            type="radio"
            name="sarja"
            bind:group={newOsallistuja.sarja}
            value="N"
        />
    </div>
    <div>
        <label for="M">Miehet</label>
        <input
            id="M"
            type="radio"
            name="sarja"
            bind:group={newOsallistuja.sarja}
            value="M"
        />
    </div>

    <button class="nappi" on:click={save}>Tallenna</button>
    <button class="nappi" on:click={clear}>Peruuta</button>
    <br />
</form>

<style>
    h1 {
        font-family: "Arial", sans-serif;
        text-align: center;
        color: black;
        border: 1px solid black;
        box-shadow: 5px 5px 15px black;
        background-color: moccasin;
    }
    form {
        display: flex;
        flex-direction: column;

        justify-content: center;
        border-collapse: collapse;
        background-color: goldenrod;
        box-shadow: 5px 5px 15px black;
        margin-left: 20%;
        margin-right: 20%;
        padding: 5%;
        padding-left: 15%;
        padding-bottom: 10%;
        width: 40%;
    }
    .syöttö {
        margin-bottom: 1em;

        padding: 0.5em;
        border: dropshadow;
        border-radius: 0.2em;
        background-color: moccasin;
        width: 60%;
    }
    .nappi {
        background-color: moccasin;
        border: dropshadow;
        border-radius: 0.2em;
        box-shadow: 5px 5px 15px black;
        width: 20%;
    }
</style>
