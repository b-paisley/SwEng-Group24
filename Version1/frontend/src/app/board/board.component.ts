import { Component, HostListener } from "@angular/core";
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
    canPromote:boolean = false;
    turn:string = "White's Turn"
    promotionPieces:string[] = ['q','r','b','n']
    
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
            if (moveStr == "E1_G1") moveStr = "O-O"
            if (moveStr == "E1_C1") moveStr = "O-O-O"
            this.piecesService.makeMove(moveStr).subscribe(data => {
                this.movePiece.reset();
                this.updateBoard(data.data.fen.toString());
                if (moveStr[4] == '8' && this.pieceArr[0][this.destSquare[0].charCodeAt(0)-65] == 'p') {
                    this.canPromote = true;
                }
                if (data.data.fen != 'error' && this.canPromote == false) {
                    this.callMitch();
                }
                if (data.data.gameOver) {
                    this.gameOver = true
                    this.turn = "You Win!"
                }
            });
        }
        
    }
    callMitch() {
        this.turn = "Black's Turn"
        this.piecesService.playPrune().subscribe(data => {
            this.updateBoard(data.data.fen.toString());
            if (data.data.gameOver) {
                this.gameOver = true
                this.turn = "MiTCh Wins!"
            } else {
                this.turn = "White's Turn"
            }
        })
    }
    doRestart(){
        this.turn = "White's Turn"
        this.gameOver = false
        this.errorMessage = false;
        this.sourceSquare = ''
        this.destSquare = ''
        this.piecesService.doRestart().subscribe(data =>{
            this.updateBoard(data.data.fen.toString());
        });
    }
    makeBoard1(){
        this.piecesService.makeBoard1().subscribe(data =>{
            this.updateBoard(data.data.fen.toString());
        });
    }
    promote(p:string) {
        this.piecesService.promote(this.sourceSquare+'_'+this.destSquare, p.toLowerCase()).subscribe(data =>{
            this.updateBoard(data.data.fen.toString());
        });
        this.canPromote = false;
        this.callMitch()
    }
}