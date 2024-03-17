<script>
    import Router from "svelte-spa-router";
    import Home from "./Home.svelte";
    import Counter from "./Counter.svelte";
    import Converter from "./Converter.svelte";
    import Weather from "./Weather.svelte";
    import Compensation from "./Compensation.svelte";
    import Participants from "./Participants.svelte";
    const routes = {
        "/": Home,
        "/Counter": Counter,
        "/Converter": Converter,
        "/Weather": Weather,
        "/Compensation": Compensation,
        "/Participants": Participants,
    };
</script>

<Router {routes} />
