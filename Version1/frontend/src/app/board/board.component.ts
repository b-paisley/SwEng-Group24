import { Component } from "@angular/core";
import { Coord } from "../class/coord";
import { PiecesService } from "../services/pieces.service";
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Piece } from "../class/piece";


import { Subject } from 'rxjs';


@Component({
    selector: "app-board",
    templateUrl: "./board.component.html",
    styleUrls: ["./board.component.css"]
})
export class BoardComponent {
    
    constructor(private piecesService: PiecesService) {  
    }
    
    sixtyFour:number[] = []
    legend:string[] = []
    numbers:number[] = []
    errorMessage:boolean = false;
    gameOver:boolean = false;
    
    
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
    movePiece = new FormGroup({
        positionMove: new FormControl('', Validators.required)
    });
    piecesSymbol = new Piece()
    sourceSquare: string = ''
    destSquare: string = ''

    onSubmit() {
        let posMove = this.movePiece.value.positionMove
        if(posMove)
        {
            this.makeMove(posMove.toString())
        }
    }

    ngOnDestroy() {
        this.destroy$.next(true);
        this.destroy$.unsubscribe();
    }

    ngOnInit() {
        this.sixtyFour = new Array(64).fill(0).map((_, i) => i);
        this.legend = ['A','B','C','D','E','F','G','H'];
        this.piecesService.getData().subscribe(data => {
            this.updateBoard(data.data.fen.toString());
        })
        this.numbers = [8,7,6,5,4,3,2,1];
    }

    updateBoard(data: string) {
        if (data == "error") {
            this.errorMessage = true;
        } else {
            this.errorMessage = false;
            this.pieceArr = data.split('/')
            for (let i = 0; i < 8; i++) {
                for (let j = 0; j < 8; j++) {
                    if (parseInt(this.pieceArr[i][j]) <= 8 && parseInt(this.pieceArr[i][j]) > 0) {
                        let blankSpace = ""
                        for (let blank = parseInt(this.pieceArr[i][j]); blank > 0; blank--) {
                            blankSpace += " "
                        }
                        let pre = 1;
                        let post = this.pieceArr.length;
                        if (j - 1 > 0) {
                            pre = j - 1
                        }
                        if (j + 1 < this.pieceArr.length) {
                            post = j + 1
                        }
                        if (j != 0 && j != this.pieceArr.length) {
                            this.pieceArr[i] = this.pieceArr[i].slice(0, post - 1) + blankSpace 
                            + this.pieceArr[i].slice(post);
                        }
                        else if (j == 0) {
                            this.pieceArr[i] = blankSpace + this.pieceArr[i].slice(1);
                        }
                        else if (j == this.pieceArr.length) {
                            this.pieceArr[i] = this.pieceArr[i].slice(0, pre) + blankSpace;
                        }
                    }
                }
            }
        }
    }

    getSymbol(letter: string) {
        return this.piecesSymbol.piecesList[letter]
    }

    isSelected(i: number): boolean {
        let x: string = String.fromCharCode(i % 8+65)
        let y = 8-Math.floor(i / 8)
        console.log(x+y)
        if (this.sourceSquare == x+y) {
            return true
        } else {
            return false
        }
    }

    storePos(i: number) {
        let x: string = String.fromCharCode(i % 8+65)
        let y = 8-Math.floor(i / 8)
        if (this.sourceSquare == '' || this.destSquare != '') { 
            this.sourceSquare = x+y
            this.destSquare = ''
        }
        else {
            this.destSquare = x+y
            this.makeMove(this.sourceSquare+'_'+this.destSquare)
        }
    }

    makeMove(moveStr: string) {
        if (!this.gameOver) {
            this.piecesService.makeMove(moveStr).subscribe(data => {
                console.log(data)
                this.movePiece.reset();
                this.updateBoard(data.data.fen.toString());
                if (data.data.gameOver) {
                    this.gameOver = true
                }
            });
        }
    }
    doRestart(){
        this.gameOver = false
        this.piecesService.doRestart().subscribe(data =>{
            console.log("enterFun");
            console.log(data.data.fen.toString());
            this.updateBoard(data.data.fen.toString());
        });
    }
}