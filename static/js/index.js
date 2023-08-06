window.onload = () => {
    feather?.replace();
}

Alpine?.store('viewer', {
    preview: null,
    result: null,
    loading: false,
    fileChosen(event) {
        this.fileToDataUrl(event, src => {
            this.preview = src;
        })
    },
    fileToDataUrl(event, callback) {
        if (! event?.target?.files?.length) return

        let file = event.target.files[0],
            reader = new FileReader()

        reader.readAsDataURL(file)
        reader.onload = e => callback(e.target.result)
    },
    async removeBg() {
        this.loading = true;
        const body = {
            "image": this.preview
        }
        const response = await axios.post("/removebg", body);
        console.log("response: ", response);
        this.loading = false;
    }
});
