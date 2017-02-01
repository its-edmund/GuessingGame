package com.mxinburritos.game.GuessingGame;

import java.util.Scanner;

public class GuessingGame {
	private int number;
	private int multiplier;
	private int guess;
	
	public GuessingGame()
	{
		System.out.println("Welcome to my guessing game.");
	}
	
	public int getNumber()
	{
		return number;
	}
	
	public void setNumber(int num)
	{
		number = num;
	}
	
	public int getMultiplier()
	{
		return multiplier;
	}
	
	public void setMultiplier(int mul)
	{
		multiplier = mul;
	}
	
	public int getGuess()
	{
		return guess;
	}
	
	public void setGuess(int g)
	{
		guess = g;
	}
	
	private void getLevel()
	{
		System.out.println("What do you want to max number to be? It must be integer.");
		while(true)
		{
			Scanner in = new Scanner(System.in);
			setMultiplier(Integer.parseInt(in.next()));
			//in.close();
			if(multiplier == (int)multiplier)
			{
				break;
			}
			else
			{
				System.out.println("Sorry. Please type in an integer.");
			}
		}
	}
	
	private void getNewNumber()
	{
		setNumber( (int) ((Math.random() * getMultiplier())));
	}
	
	private void getAndCheckGuess()
	{
		while(true)
		{
			System.out.println("Type in your guess.");
			Scanner g = new Scanner(System.in);
			setGuess(Integer.parseInt(g.next()));
			//g.close();
			if(getGuess() == getNumber())
			{
				winGame();
			}
			else if(getGuess() < getNumber())
			{
				System.out.println("Sorry. Too low! Try again!");
			}
			else if(getGuess() > getNumber())
			{
				System.out.println("Sorry. Too high! Try again!");
			}
		}
	}
	
	private void winGame()
	{
		System.out.println("You guessed the number! Nice Job!");
		System.out.println("Would you like to play again? Y/N?");
		while(true)
		{
			Scanner ans = new Scanner(System.in);
			String answer = ans.next();
			ans.close();
			if(answer.equalsIgnoreCase("Y"))
			{
				game();
				break;
			}
			else if(answer.equalsIgnoreCase("N"))
			{
				System.exit(0);
			}
			else
			{
				System.out.println("Sorry. I'm not sure what you typed. Please try again!");
			}
		}
	}
	
	public void game()
	{
		getLevel();
		getNewNumber();
		getAndCheckGuess();
	}
}
