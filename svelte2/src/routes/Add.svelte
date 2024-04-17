<script>
    import { onMount } from "svelte";
    let m_title, m_body, m_userId;
    let users = [];
    let user = {};

    onMount(getUser);

    function save() {
        m_userId = user;

        fetch(`https://jsonplaceholder.typicode.com/posts`, {
            method: "POST",
            body: JSON.stringify({
                title: m_title,
                body: m_body,
                userId: m_userId,
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                console.log("json from save()", json);
                (m_title = ""), (m_body = ""), (m_userId = "");
                alert(`Post \"${json.title}\" saved`);
            });
    }
    function getUser() {
        fetch("https://jsonplaceholder.typicode.com/users", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                users = json;
            });
    }
</script>

<h1>Add</h1>
<form>
    <div>
        <span>Title</span>
        <input bind:value={m_title} />
    </div>
    <div>
        <span>Body</span>
        <input bind:value={m_body} />
    </div>
    <div>
        <span>User</span>

        <select bind:value={user}>
            {#each users as user}
                <option value={(user.name, user.id)}>{user.name}</option>
            {/each}
        </select>
    </div>
    <button on:click={save}>Save</button>
</form>

<style>
    span {
        display: inline-block;
        width: 80px;
        font-weight: bold;
    }
    div {
        margin: 8px;
    }
</style>
