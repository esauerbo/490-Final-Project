export class Counties {
    constructor() {
        this.file = 'https://raw.githubusercontent.com/comalvirdi/490Files/main/county_demographics.csv'
        this.data = this.convertData()
    }

    convertData() {
        const reader = new FileReader();
        return reader.readAsText(this.file);
    }

}
