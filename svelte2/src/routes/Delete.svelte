<script>
    import { onMount } from "svelte";
    let posts = [];
    let post = {
        title: "",
        id: "",
    };

    onMount(get);

    function get() {
        fetch("https://jsonplaceholder.typicode.com/posts", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((json) => {
                posts = json;
            });
    }

    function yeet() {
        fetch(`https://jsonplaceholder.typicode.com/posts/${post.id}`, {
            method: "DELETE",
        });
        alert(`Post \"${post.title}\" deleted`);
    }
</script>

<h1>Delete</h1>

<h2>Select a post to be deleted.</h2>
<select bind:value={post}>
    {#each posts as post}
        <option title={post.title} value={post}>
            {post.title.substring(0, 20)}...
        </option>
    {/each}
</select>
<button on:click={yeet}> Delete </button>
