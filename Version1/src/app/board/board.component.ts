import { Component } from "@angular/core";
import { Coord } from "./coord";
import { PiecesService } from "../pieces.service";
import { Piece } from "./piece/piece";
import { takeUntil } from 'rxjs/operators';

import { Subject } from 'rxjs';


@Component({
    selector: "app-board",
    templateUrl: "./board.component.html",
    styleUrls: ["./board.component.css"]
})
export class BoardComponent {

    sixtyFour = new Array(64).fill(0).map((_, i) => i);

    // sconstructor(private pieces: PiecesService) {}

    xy(i: number) {
        return {
            x: i % 8,
            y: Math.floor(i / 8)
        }
    }

    isBlack({ x, y }: Coord) {
        return (x + y) % 2 === 1;
    }
    destroy$: Subject<boolean> = new Subject<boolean>();
    pieceArr: any[] = [];

    ngOnDestroy() {
        this.destroy$.next(true);
        this.destroy$.unsubscribe();
    }

    constructor(private pieces: PiecesService) {
        this.pieces.getData().subscribe(data => {
            this.pieceArr = Object.values(data)[0]
            console.log(this.pieceArr)
        })
    }

}