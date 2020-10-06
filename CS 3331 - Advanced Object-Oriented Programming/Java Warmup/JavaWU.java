/*
Title: Java Warmup
Author: Jorge Favela
*/
import java.util.Scanner;

class JavaWU{

    //Attributes------------------------------------------------------------------------------------------
    String edgeAdj="";
    String cornerAdj="";
    String notAdj="";

    //Constructors---------------------------------------------------------------------------------------- 
    JavaWU(){}

    JavaWU(String col, int row, int len, String s){ //creates JavaWU object from a letter and a number
        String e = eAdj(ltr2num(col),row);
        String c = cAdj(ltr2num(col),row);
        String n = nAdj(e+c);
        switch(len){
            case 2:
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+num2ltr(e.substring(i,i+1))+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+num2ltr(c.substring(i,i+1))+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+num2ltr(n.substring(i,i+1))+n.substring(i+1,i+2)+") ";
                }
                break;

            case 3:
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+num2ltr(e.substring(i,i+1))+s+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+num2ltr(c.substring(i,i+1))+s+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+num2ltr(n.substring(i,i+1))+s+n.substring(i+1,i+2)+") ";
                }
                break;

            case 5:
                //Formats the 3 resulting strings of coordinates to look nicer
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+num2ltr(e.substring(i,i+1))+","+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+num2ltr(c.substring(i,i+1))+","+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+num2ltr(n.substring(i,i+1))+","+n.substring(i+1,i+2)+") ";
                }
                break;
                
            case 6:
                //Formats the 3 resulting strings of coordinates to look nicer
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+num2ltr(e.substring(i,i+1))+", "+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+num2ltr(c.substring(i,i+1))+", "+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+num2ltr(n.substring(i,i+1))+", "+n.substring(i+1,i+2)+") ";
                }
                break;
        }
    }

    JavaWU(int col, int row, int len, String s){ //creates JavaWU object from 2 numbers
        String e = eAdj(col,row);
        String c = cAdj(col,row);
        String n = nAdj(e+c);
        switch(len){
            case 2:
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+e.substring(i,i+1)+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+c.substring(i,i+1)+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+n.substring(i,i+1)+n.substring(i+1,i+2)+") ";
                }
                break;
            
            case 3:
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+e.substring(i,i+1)+s+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+c.substring(i,i+1)+s+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+n.substring(i,i+1)+s+n.substring(i+1,i+2)+") ";
                }
                break;
            case 5:
                //Formats the 3 resulting strings of coordinates to look nicer
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+e.substring(i,i+1)+","+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+c.substring(i,i+1)+","+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+n.substring(i,i+1)+","+n.substring(i+1,i+2)+") ";
                }
                break;
                
            case 6:
                //Formats the 3 resulting strings of coordinates to look nicer
                for(int i=0; i<e.length(); i=i+2){
                    this.edgeAdj =this.edgeAdj + "("+e.substring(i,i+1)+", "+e.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<c.length(); i=i+2){
                    this.cornerAdj =this.cornerAdj + "("+c.substring(i,i+1)+", "+c.substring(i+1,i+2)+") ";
                }
                for(int i=0; i<n.length(); i=i+2){
                    this.notAdj =this.notAdj + "("+n.substring(i,i+1)+", "+n.substring(i+1,i+2)+") ";
                }
                break;
        }
    }

    //Converters------------------------------------------------------------------------------------------
    
    public int ltr2num(String l){
        String[] ltrs = {"a","b","c","d","e","f","g","h","i"};
        for(int i=0; i<9; i++){
            if(l.equals(ltrs[i])){
                return i;
            }
        }
        return -1;
    }

    public String num2ltr(String num){
        String[] ltrs = {"a","b","c","d","e","f","g","h","i"};
        return ltrs[Integer.parseInt(num)];
    }

    //Helper Methods--------------------------------------------------------------------------------------

    /*
        The following methods return a single string of coordinates in the following format:
        (r=row coordinate, c=column coordinate) rcrcrcrcrcrcrcrcrcrcrc
    */

    public String eAdj(int row, int col){ //Method finds all the edge-adjacent squares and returns a string containing their coordinates
        String adjS = "";

        //Each if statement makes sure the square is within the bounds of the board
        if(row-1>=0){
            adjS= adjS+Integer.toString(row-1)+Integer.toString(col);
        }
        if(col-1>=0){
            adjS= adjS+Integer.toString(row)+Integer.toString(col-1);
        }
        if(col+1<=8){
            adjS= adjS+Integer.toString(row)+Integer.toString(col+1);
        }
        if(row+1<=8){
            adjS= adjS+Integer.toString(row+1)+Integer.toString(col);
        }
        return adjS;
    } 

    public String cAdj(int row, int col){ //Method finds all the corner-adjacent squares and returns a string containing their coordinates
        String adjS = "";

        //Each if statement makes sure the square is within the bounds of the board
        if(row-1>=0 && col-1>=0){
            adjS= adjS+Integer.toString(row-1)+Integer.toString(col-1);
        }
        if(row-1>=0 && col+1<=8){
            adjS= adjS+Integer.toString(row-1)+Integer.toString(col+1);
        }
        if(row+1<=8 && col-1>=0){
            adjS= adjS+Integer.toString(row+1)+Integer.toString(col-1);
        }
        if(col+1<=8 && row+1<=8){
            adjS= adjS+Integer.toString(row+1)+Integer.toString(col+1);
        }
        return adjS;
    }

    public String nAdj(String adj){  //Method finds all the non-adjacent squares and returns a string containing their coordinates
        String nAdj="";

        /*Gives starting points for finding the row and column coordinates min and max values to serve as a guide for which squares
        not to add to the list*/
        int rMin= Integer.parseInt(adj.substring(0,1));
        int rMax= Integer.parseInt(adj.substring(0,1));
        int cMin= Integer.parseInt(adj.substring(1,2));
        int cMax= Integer.parseInt(adj.substring(1,2));

        //for loop goes through the first 2 lists of adj squares and determins the min and max valuse held by the row indexs and the column indexs
        for(int i=0; i<adj.length()-1; i=i+2){
            int j=i+1;
            int v1;
            int v2;
            if(j==adj.length()-1){
                v1= Integer.parseInt(adj.substring(i,i+1));
                v2= Integer.parseInt(adj.substring(j));
            }
            else{
                v1= Integer.parseInt(adj.substring(i,i+1));
                v2= Integer.parseInt(adj.substring(j,j+1));
            }

            //These 4 if statements take care of the checks and reassigning if necessary
            if(v1<rMin){rMin=v1;}
            if(v1>rMax){rMax=v1;}
            if(v2<cMin){cMin=v2;}
            if(v2>cMax){cMax=v2;}
        }

        /*Finally, These nested for loops add all the non-adjacent squares while using the min and max values to 
        avoid adding any that have already been determined to be adjacent*/
        for(int i=8; i>-1; i--){
            for(int j=0; j<9; j++){
                if(i>=rMin && i<=rMax){
                    if(!(j>=cMin && j<=cMax)){
                        nAdj = nAdj + Integer.toString(i) + Integer.toString(j);
                    }
                }
                else{
                    nAdj = nAdj + Integer.toString(i) + Integer.toString(j);
                }
            }
        }
        return nAdj;
    }
    public static void main(String[] args){
        Scanner scnr = new Scanner(System.in);
        System.out.print("Enter square coordinates('x' to exit): ");
        String sqr = scnr.nextLine();

        while(!sqr.equals("x")){ //While loop to continue inputting different values until satisfied
            //Program uses the length of input to determine the which constructor is likely to be used
            if(sqr.length()>=5){ 
                if(Character.isDigit(sqr.charAt(1))){ //I added this little check just to expand on the possible inputs it could handle
                    int col = Integer.parseInt(sqr.substring(1,2));
                    int row = Integer.parseInt(sqr.substring(sqr.length()-2,sqr.length()-1));
                    JavaWU shot = new JavaWU(row,col,sqr.length(), ""); //Creates sqr object
                    
                    //Displays the values
                    System.out.println("\nSquare coordinates: "+sqr);
                    System.out.println("\nEdge-adjacent squares: " + shot.edgeAdj);
                    System.out.println("\nCorner-adjacent squares: " + shot.cornerAdj);
                    System.out.println("\nNon-adjacent square: " + shot.notAdj);
                }
                else{ //If col coordinate is a letter
                    //stores values as a string and an int instead of 2 ints
                    String col = sqr.substring(1,2);
                    int row = Integer.parseInt(sqr.substring(sqr.length()-2,sqr.length()-1));
                    JavaWU shot = new JavaWU(col,row,sqr.length(),"");

                    //Displays the values
                    System.out.println("\nSquare coordinates: "+sqr);
                    System.out.println("\nEdge-adjacent squares: " + shot.edgeAdj);
                    System.out.println("\nCorner-adjacent squares: " + shot.cornerAdj);
                    System.out.println("\nNon-adjacent square: " + shot.notAdj);
                }
            }
            else if(sqr.length()==3){ //Length of 3 could have various different possibilities
                //Example: f 5  5 5  5,5
                if(Character.isDigit(sqr.charAt(0))){ //checks if row index is a number
                    int col = Integer.parseInt(sqr.substring(0,1));
                    int row = Integer.parseInt(sqr.substring(2));
                    JavaWU shot = new JavaWU(row,col,sqr.length(),sqr.substring(1,2));

                    //Displays the values
                    System.out.println("\nSquare coordinates: "+sqr);
                    System.out.println("\nEdge-adjacent squares: " + shot.edgeAdj);
                    System.out.println("\nCorner-adjacent squares: " + shot.cornerAdj);
                    System.out.println("\nNon-adjacent square: " + shot.notAdj);
                }
                else{
                    String col = sqr.substring(0,1);
                    int row = Integer.parseInt(sqr.substring(2));
                    JavaWU shot = new JavaWU(col,row, sqr.length(),sqr.substring(1,2));

                    //Displays the values
                    System.out.println("\nSquare coordinates: "+sqr);
                    System.out.println("\nEdge-adjacent squares: " + shot.edgeAdj);
                    System.out.println("\nCorner-adjacent squares: " + shot.cornerAdj);
                    System.out.println("\nNon-adjacent square: " + shot.notAdj);
                }
            }
            else{ //
                //row is a letter and col is a number
                String col = sqr.substring(0,1);
                int row = Integer.parseInt(sqr.substring(1));
                JavaWU shot = new JavaWU(col,row,sqr.length(),"");

                //Displays the values
                System.out.println("\nSquare coordinates: "+sqr);
                System.out.println("\nEdge-adjacent squares: " + shot.edgeAdj);
                System.out.println("\nCorner-adjacent squares: " + shot.cornerAdj);
                System.out.println("\nNon-adjacent square: " + shot.notAdj);
            }
            
            //Checks if user wants to exit the program or input other values
            System.out.println("--------------------------------------------------------------------------------------------------------------\n\n");
            System.out.print("Enter square coordinates('x' to exit): ");
            sqr = scnr.nextLine();
            }
        System.out.println("Have a nice day! Goodbye :)"); 
        scnr.close();
    }


}
