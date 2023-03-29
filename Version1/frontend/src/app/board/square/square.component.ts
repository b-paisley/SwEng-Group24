import { Component, Input } from "@angular/core";

@Component({
    selector: 'app-square',
    templateUrl: './square.component.html',
    styleUrls: [`square.component.css`]
})
export class SquareComponent {
    @Input()
    black!: boolean;

    getStyle() {
        return this.black
            ? { backgroundColor: '#b48866' }
            : { backgroundColor: '#efd8b6' };
    }
}