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
            console.log(data)
            this.pieceArr = Object.values(data).toString().split('/')
            console.log(this.pieceArr[6].slice(0,1))
            console.log(this.pieceArr[6].slice(2))
            for (let i = 0; i < 8; i++) {
                for(let j = 0; j < 8; j++) {
                    if (parseInt(this.pieceArr[i][j]) <= 8 && parseInt(this.pieceArr[i][j]) > 0) {
                        let blankSpace = ""
                        for (let blank = parseInt(this.pieceArr[i][j]); blank > 0; blank--) {
                            blankSpace +=  " "
                        }
                        let pre = 1;
                        let post = this.pieceArr.length-1;
                        if (j-1 > 0) pre = j-1
                        if (j+1 < this.pieceArr.length) post = j+1
                        console.log(this.pieceArr[i][j] + ' ' + pre + ' ' + post + ' ' + j)
                        if (j != 0 && j != this.pieceArr.length) this.pieceArr[i] = this.pieceArr[i].slice(0, post-1) + blankSpace + this.pieceArr[i].slice(post);
                        else if (j == 0) this.pieceArr[i] = blankSpace + this.pieceArr[i].slice(1);
                        else if (j == this.pieceArr.length) this.pieceArr[i] = this.pieceArr[i].slice(0, pre) + blankSpace;
                    }
                }
            }
            console.log(this.pieceArr)
        })
    }

}