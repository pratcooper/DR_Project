/* =======================================
 * JFreeChart : a Java Chart Class Library
 * =======================================
 *
 * Project Info:  http://www.jrefinery.com/jfreechart
 * Project Lead:  David Gilbert (david.gilbert@jrefinery.com);
 *
 * (C) Copyright 2000-2002, by Simba Management Limited and Contributors.
 *
 * This library is free software; you can redistribute it and/or modify it under the terms
 * of the GNU Lesser General Public License as published by the Free Software Foundation;
 * either version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
 * without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License along with this
 * library; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330,
 * Boston, MA 02111-1307, USA.
 *
 * ---------
 * Tick.java
 * ---------
 * (C) Copyright 2000-2002, by Simba Management Limited.
 *
 * Original Author:  David Gilbert (for Simba Management Limited);
 * Contributor(s):   -;
 *
 * $Id: Tick.java,v 1.2 2001/09/18 05:48:48 mungady Exp $
 *
 * Changes (from 18-Sep-2001)
 * --------------------------
 * 18-Sep-2001 : Added standard header and fixed DOS encoding problem (DG);
 *
 */

package com.jrefinery.chart;

import java.util.*;

/**
 * Represents the dimensions of a tick on an axis (used during the process of drawing a chart,
 * but not retained).
 */
public class Tick {

    /** The tick value. */
    protected Object value;

    /** A text version of the tick value. */
    protected String text;

    /** The x-coordinate of the tick. */
    protected float x;

    /** The y-coordinate of the tick. */
    protected float y;

    /**
     * Standard constructor: creates a Tick with the specified properties.
     * @param value The tick value;
     * @param formattedValue The formatted version of the tick value;
     * @param x The x-coordinate of the tick;
     * @param y The y-coordinate of the tick;
     */
    public Tick(Object value, String text, float x, float y) {
	this.value = value;
	this.text = text;
	this.x=x;
	this.y=y;
    }

    /**
     * Standard constructor: creates a Tick with the specified properties.
     * @param formattedValue The formatted version of the tick value;
     * @param x The x-coordinate of the tick;
     * @param y The y-coordinate of the tick;
     */
    public Tick(String text, float x, float y) {
	this(text, text, x, y);
    }

    /**
     * Returns the numerical value of the tick, or null if the value is not a Number.
     * @return The tick value.
     */
    public double getNumericalValue() {

	if (value instanceof Number) {
            Number x = (Number)value;
	    return x.doubleValue();
	}
	else if (value instanceof Date) {
            Date x = (Date)value;
	    return (double)x.getTime();
	}
	else return 0.0;
    }

    /**
     * Returns the text version of the tick value.
     * @return The formatted version of the tick value;
     */
    public String getText() {
	return text;
    }

    /**
     * Returns the x-coordinate of the tick.
     * @return The x-coordinate of the tick.
     */
    public float getX() {
	return x;
    }

    /**
     * Returns the y-coordinate of the tick.
     * @return The y-coordinate of the tick.
     */
    public float getY() {
	return y;
    }

}
