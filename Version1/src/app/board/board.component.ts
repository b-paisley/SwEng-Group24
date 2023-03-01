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
    pieceArr: string[] = [];

    ngOnDestroy() {
        this.destroy$.next(true);
        this.destroy$.unsubscribe();
    }

    constructor(private pieces: PiecesService) {
        this.pieces.getData().subscribe(data => {
            this.pieceArr = Object.values(data).toString().split('/')
            for (let i = 0; i < 8; i++) {
                for(let j = 0; j < 8; j++) {
                    if (parseInt(this.pieceArr[i][j]) <= 8 && parseInt(this.pieceArr[i][j]) > 0) {
                        let blankSpace = ""
                        for (let blank = parseInt(this.pieceArr[i][j]); blank > 0; blank--) {
                            blankSpace +=  " "
                        }
                        this.pieceArr[i] = this.pieceArr[i].slice(0,j) + blankSpace;
                    }
                }
            }
        })
    }

}